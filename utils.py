import requests

def create_lnbits_invoice(amount, memo, lnbits_url, lnbits_api_key):
    """
    Create an invoice on the LNbits platform.

    Args:
        amount (int): The invoice amount in satoshis.
        memo (str): A description or note for the invoice.
        lnbits_url (str): The base URL of the LNbits API.
        lnbits_api_key (str): The API key for the LNbits account.

    Returns:
        dict: The LNbits invoice details.
    """
    invoice_details = {
        "out": False,
        "amount": amount,
        "memo": memo
    }

    headers = {"X-Api-Key": lnbits_api_key}
    url = f"{lnbits_url}/api/v1/payments"

    lnbits_invoice = requests.post(url, headers=headers, json=invoice_details).json()
    
    return lnbits_invoice
