document.addEventListener("DOMContentLoaded", () => {
    let loginBtn = document.getElementById("login");
    let singinBtn = document.getElementById("sign_in");
    let passwordBtn = document.getElementById("Password_sign_in");
    let passwordAgainBtn = document.getElementById("Passwordagain_sign_in");
    let incomeBtn = document.getElementById("Income_input");
    let outcomeBtn = document.getElementById("Outcome_input");
    let addOutcomeBtn = document.getElementById("Add_outcome");
    let addIncomeBtn = document.getElementById("Add_income");
    let settingsBtn = document.getElementById("Settings");
    let clearValues_outcomeBtn = document.getElementById("clearValues_outcome");
    let clearValues_incomeBtn = document.getElementById("clearValues_income");
    let closePopup_incomeBtn = document.getElementById("closePopupBtn_income");
    let closePopup_outcomeBtn = document.getElementById("closePopupBtn_outcome");
    let popup_income = document.getElementById("popup_income");
    let popup_outcome = document.getElementById("popup_outcome");
    let show_inputBtn = document.getElementById("Income_input");
    let show_outcomeBtn = document.getElementById("outcome_input");
    let popup_settings = document.getElementById("popup_settings");
    let clearValues_settingsBtn = document.getElementById("clearValues_settings");
    let closePopup_settingsBtn = document.getElementById("closePopupBtn_settings");
    let addSettingsBtn = document.getElementById("Settings");


    // Event listeners
    if (addSettingsBtn) addSettingsBtn.addEventListener("click", Add_setting);
    if (closePopup_settingsBtn) closePopup_settingsBtn.addEventListener("click", closePopup_settings);
    if (clearValues_settingsBtn) clearValues_settingsBtn.addEventListener("click", clearValues_settings);

    if (show_inputBtn) show_inputBtn.addEventListener("change", showing_income);
    if (show_outcomeBtn) show_outcomeBtn.addEventListener("change", showing_outcome);
    if (closePopup_incomeBtn) closePopup_incomeBtn.addEventListener("click", closePopup_income);
    if (closePopup_outcomeBtn) closePopup_outcomeBtn.addEventListener("click", closePopup_outcome);
    if (loginBtn) loginBtn.addEventListener("click", login);
    if (singinBtn) singinBtn.addEventListener("click", sign_in);
    if (incomeBtn) incomeBtn.addEventListener("click", income);
    if (outcomeBtn) outcomeBtn.addEventListener("click", outcome);
    if (addOutcomeBtn) addOutcomeBtn.addEventListener("click", Add_outcome);
    if (addIncomeBtn) addIncomeBtn.addEventListener("click", Add_income);
    if (settingsBtn) settingsBtn.addEventListener("click", settings);
    if (clearValues_incomeBtn) clearValues_incomeBtn.addEventListener("click", clearValues_income);
    if (clearValues_outcomeBtn) clearValues_outcomeBtn.addEventListener("click", clearValues_outcome);
    if (passwordBtn && passwordAgainBtn) {
        passwordAgainBtn.addEventListener("change", check_password);
    }

    // Functions
    function login() {
        window.open("/login", "_self");
    }

    function sign_in() {
        window.open("/sign_in", "_self");
    }

    function check_password() {
        if (passwordBtn.value !== passwordAgainBtn.value) {
            alert("Passwords don't match");
        }
    }

    function income() {
        console.log("Income function triggered");
    }

    function outcome() {
        console.log("Outcome function triggered");
    }

    function settings() {
        console.log("Settings function triggered");
    }

    function Add_setting() {
        if (popup_settings) popup_settings.style.display = "block";
    }

    function closePopup_settings() {
        if (popup_settings) popup_settings.style.display = "none";
    }

    function clearValues_settings() {
        document.getElementById("change_password").value = "";
    }

    function Add_income() {
        console.log("check");
        if (popup_income) popup_income.style.display = "block";
    }

    function closePopup_income() {
        if (popup_income) popup_income.style.display = "none";
    }

    function clearValues_income() {
        document.getElementById("income_amount").value = "";
        document.getElementById("details_income").value = "";
        document.getElementById("date_income").value = "";
        document.getElementById("category_income").value = "";
    }

    function Add_outcome() {
        if (popup_outcome) popup_outcome.style.display = "block";
    }

    function closePopup_outcome() {
        if (popup_outcome) popup_outcome.style.display = "none";
    }

    function clearValues_outcome() {
        document.getElementById("outcome_amount").value = "";
        document.getElementById("details_outcome").value = "";
        document.getElementById("date_outcome").value = "";
        document.getElementById("category_outcome").value = "";
    }


    function deleteIncome(id) {
        fetch("/delete-income", {
          method: "POST",
          body: JSON.stringify({ id: id }),
        }).then((_res) => {
          window.location.href = "/user_data";
        });
    }

    document.querySelectorAll(".close").forEach((button) => {
        button.addEventListener("click", () => {
          const id = button.getAttribute("data-id");
          deleteIncome(id);
        });
      });

    function deleteOutcome(id) {
        fetch("/delete-outcome", {
          method: "POST",
          body: JSON.stringify({ id: id }),
        }).then((_res) => {
          window.location.href = "/";
        });
    }



    function showing_income() {
        if (show_inputBtn.checked === true) {
            window.location.href = "/user_data?income=true";
        } else {
            window.location.href = "/user_data?income=false";
        }
    }
    
    function showing_outcome() {
        if (show_outcomeBtn.checked === true) {
            window.location.href = "/user_data?outcome=true";
        } else {
            window.location.href = "/user_data?outcome=false";
        }
    }
    
});
