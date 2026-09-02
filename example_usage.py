from client import UniversalAgenticCartCheckoutBrokerClient

def main():
    client = UniversalAgenticCartCheckoutBrokerClient()
    res = client.broker_multi_merchant_cart([{'sku': 'MONITOR_OLED_32', 'quantity': 1, 'merchant_domain': 'techstore.com'}])
    print('Universal Agentic Cart Broker: ' + res['federated_cart_id'] + ' (' + str(res['merchants_involved_count']) + ' merchants)')
    print('Subtotal: $' + str(res['items_subtotal_usd']) + ' | Shipping: $' + str(res['consolidated_shipping_usd']))
    print('Checkout Session: ' + res['universal_checkout_session_url'])
    print('Handoff Token: ' + res['agent_handoff_token'])

if __name__ == '__main__':
    main()
