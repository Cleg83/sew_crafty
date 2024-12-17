document.addEventListener("DOMContentLoaded", function () {
    const useProfileCheckbox = document.getElementById("use_profile_info");
    const fetchProfileInfoURL = useProfileCheckbox.dataset.fetchUrl;

    // Get form field elements by their IDs
    const emailField = document.getElementById("id_email");
    const phoneField = document.getElementById("id_phone_number");
    const address1Field = document.getElementById("id_address_1");
    const address2Field = document.getElementById("id_address_2");
    const townField = document.getElementById("id_town");
    const countyField = document.getElementById("id_county");
    const postcodeField = document.getElementById("id_postcode");

    // Event listener for checkbox change
    useProfileCheckbox.addEventListener("change", function () {
        if (useProfileCheckbox.checked) {
            // Fetch profile data from the server
            fetch(fetchProfileInfoURL)
                .then(response => {
                    if (!response.ok) {
                        throw new Error("Failed to fetch profile data");
                    }
                    return response.json();
                })
                .then(data => {
                    if (data.error) {
                        console.error("Error:", data.error);
                        return;
                    }
                    // Populate form fields with fetched data
                    emailField.value = data.email || "";
                    phoneField.value = data.phone_number || "";
                    address1Field.value = data.address_1 || "";
                    address2Field.value = data.address_2 || "";
                    townField.value = data.town || "";
                    countyField.value = data.county || "";
                    postcodeField.value = data.postcode || "";
                })
                .catch(error => {
                    console.error("Error fetching profile info:", error);
                });
        } else {
            // Clear fields if the checkbox is unchecked
            emailField.value = "";
            phoneField.value = "";
            address1Field.value = "";
            address2Field.value = "";
            townField.value = "";
            countyField.value = "";
            postcodeField.value = "";
        }
    });
});
