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

    // From using {% csrf_token %} in the form
    var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
    };
    var url = '/checkout/cache_checkout_data/';

    // Concatenate first and last name form fields into fullName for below function
    const firstName = form.first_name.value.trim();
    const lastName = form.last_name.value.trim();
    const fullName = `${firstName} ${lastName}`.trim();


    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: fullName,
                    phone: form.phone_number.value.trim(),
                    email: form.email.value.trim(),
                    address: {
                        line1: form.address_1.value.trim(),
                        line2: form.address_2.value.trim(),
                        city: form.town.value.trim(),
                        state: form.county.value.trim(),
                        country: form.country.value.trim(),
                    }
                }
            },
            shipping_details: {
                name: fullName,
                phone: form.phone_number.value.trim(),
                address: {
                    line1: form.address_1.value.trim(),
                    line2: form.address_2.value.trim(),
                    city: form.town.value.trim(),
                    state: form.county.value.trim(),
                    postal_code: form.postcode.value.trim(),
                    country: form.country.value.trim(),
                }
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
    }).fail(function () {
        location.reload();
    })
});

