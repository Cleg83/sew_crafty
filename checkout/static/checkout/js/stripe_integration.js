var stripePublic = $('#id_stripe_public').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublic);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
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
card.mount('#payment-info-box');

// Handle card validation errors 
card.addEventListener('change', function (event) {
    var paymentErrorDiv = document.getElementById('payment-error-box');
    if (event.error) {
        var html = `
            <span class="text-danger">${event.error.message}</span>
        `;
        paymentErrorDiv.innerHTML = html;
    } else {
        paymentErrorDiv.textContent = '';
    }
});

// Payment form submission 

var form = document.getElementById('checkout-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true });
    document.getElementById('submit-button').disabled = true;

    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorBox = document.getElementById('payment-error-box');
            var html = `
                <span>${result.error.message}</span>`;
            errorBox.innerHTML = html;
            card.update({ 'disabled': false });
            document.getElementById('submit-button').disabled = false;
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});

