import os 
import dotenv 

import stripe

#consfiguracion de stripe
dotenv.load_dotenv()


STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")


stripe.api_key = STRIPE_SECRET_KEY
#creacion de un metodo de pago
def create_payments_method() -> str: 
    try:
        payment_method = stripe.PaymentMethod.create(
            type="card",
            card={"token": "tok_visa"},
        )

        print("metodo de pago creado con ID:{payment_method.id}")
        
        return payment_method.id
    except stripe.error.CardError as e:
        print("error al crear el metodo de pago: {e.user_message}")
        

#crear un pago

def create_payment(payment_method_id: str):
   try:

        payment = stripe.PaymentIntent.create(
            amount=5 * 100,
            currency="usd",
            payment_method=payment_method_id,
            payment_method_types=["card"],
            confirm=True,
        )


        print(f'pago creado con ID: {payment.id}')

   except stripe.error.CardError as e:
        print(f"error al crear el pago: {e.user_message}")

    


payment_method_id = create_payments_method()

create_payment(payment_method_id)