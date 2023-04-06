import unittest
import responses
from utils import create_lnbits_invoice

class TestCreateLnbitsInvoice(unittest.TestCase):

    @responses.activate
    def test_create_lnbits_invoice(self):
        # Mock the LNbits API response
        lnbits_url = "https://lnbits.example.com"
        lnbits_api_key = "test_api_key"
        invoice_details = {
            "out": False,
            "amount": 1000,
            "memo": "Test invoice"
        }
        mocked_response = {
            "payment_hash": "3d852d12946b4893d241de9e48c6ae28749f0cbc6e650a60f60eab58cdc38a81",
            "payment_request": "lnbc400n1pjznh45sp56qsj840ttycmksaku73afh7hhaqpuhay9nse7wwvfst348q2" + \
                                "nswqpp58kzj6y55ddyg85jpm60y334w9pef7rxvde5q5c8kp6443nwr32qsdqzvcxqzjc" + \
                                "cqpjrzjq2ajfk3ap7c8j06frrr4n8uh8nzq9uy39mplk5cywrclcz9a6mkt2zmv2vqq9xq" + \
                                "qqgqqqqqpqqqqq8sq9q9qyysgq6nm57wqere5tmxdlgdncdrtvj0474jkegr3w9kmecm3nj" + \
                                "q99f25x8h74ermgu733n9u8uw0rrlrj8g287yz04902qcwhpp7dnns8lxspk5vz4t"
        }

        responses.add(responses.POST, f"{lnbits_url}/api/v1/payments",
                      json=mocked_response, status=200)

        # Call the create_lnbits_invoice function
        lnbits_invoice = create_lnbits_invoice(invoice_details["amount"], invoice_details["memo"],
                                               lnbits_url, lnbits_api_key)

        # Check if the function returns the expected data
        self.assertEqual(lnbits_invoice["payment_hash"], mocked_response["payment_hash"])
        self.assertEqual(lnbits_invoice["payment_request"], mocked_response["payment_request"])

if __name__ == '__main__':
    unittest.main()
