var stripePublic = $('#id_stripe_public').text().slice(1, -1);
var stripeSecret = $('#id_stripe_secret').text().slice(1, -1);
var stripe = Stripe(stripePublic);
var elements = stripe.elements();
var style = {
    base: {
        color: '#212529',
        fontFamily: '"Quicksand", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = elements.create('card', {style: style});
card.mount('#card-element');