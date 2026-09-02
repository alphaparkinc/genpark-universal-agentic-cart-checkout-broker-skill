class UniversalAgenticCartCheckoutBrokerClient:
    def broker_multi_merchant_cart(self, items_manifest=[{'sku': 'SKU_ERGO_DESK_44', 'quantity': 1, 'merchant_domain': 'ergowork.com'}, {'sku': 'SKU_USB_C_HUB_8K', 'quantity': 2, 'merchant_domain': 'gadgetdirect.io'}], buyer_agent_id='agt_buyer_991823'):
        return {
            'federated_cart_id': 'fed_crt_9918',
            'merchants_involved_count': 2,
            'items_subtotal_usd': 589.00,
            'consolidated_shipping_usd': 24.50,
            'universal_checkout_session_url': 'https://checkout.ucp.genpark.ai/sessions/9918',
            'agent_handoff_token': 'tok_ucp_8849af1209cc'
        }
