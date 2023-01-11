import mercadopago

sdk = mercadopago.SDK("APP_USR-1417871520882408-010918-ee34d47e6a3de97b668777912b34bdf0-494625348")

def createPayment(idChat, nome):
    
    payment_data = {
        "transaction_amount": 29.90,
        "description": f"[Mensalidade | Sigma Bet Bot] - {nome}",
        "payment_method_id": "pix",
        "payer": {
            "email": f"{nome}{idChat}_sigmabet@gmail.com",
            "first_name": f"{nome}",
            "last_name": f"{nome}",
        }
    }

    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]
    
    paymentObj = {
        "idPagamento": f"{payment['id']}",
        "nomeGateway": "Mercado Pago",
        "pagador": f"{nome}",
        "valor": f"{payment['transaction_amount']}",
        "descPagamento": f"{payment['description']}",
        "chavePix": f"{payment['point_of_interaction']['transaction_data']['qr_code']}",
        "detalhesPag": f"{payment['point_of_interaction']['transaction_data']['ticket_url']}"
    }

    print(paymentObj)
    return(paymentObj)

def statusPayment(id):

    payment_response = sdk.payment().get(id)
    paymentStatus = payment_response["response"]
    print(paymentStatus['status'])