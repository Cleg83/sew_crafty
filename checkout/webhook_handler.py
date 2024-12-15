from django.http import HttpResponse

class WH_Handler:
    """Handles stripe webhooks"""

    def __init__(self, request):
      self.request = request

    def handle_event(self, event):
      """
      Handles generic events from stripe 
      """
      return HttpResponse(
        content=f'Webhook received: {event("type")}',
        status=200)
    
    def handle_payment_intent_succeeded(self, event):
      """
      Handles payment_intent.succeeded webhook from stripe
      """
      return HttpResponse(
        content=f'Webhook received: {event("type")}',
        status=200)
    
    def handle_payment_intent_payment_failed(self, event):
      """
      Handles payment_intent.payment_failed webhook from stripe
      """
      return HttpResponse(
        content=f'Webhook received: {event("type")}',
        status=200)
    

