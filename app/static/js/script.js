document.addEventListener("DOMContentLoaded", () => {
    let loginBtn = document.getElementById("login");
    let singinBtn = document.getElementById("sign_in");
    let passwordBtn = document.getElementById("Password_sign_in");
    let passwordAgainBtn = document.getElementById("Passwordagain_sign_in");
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
    let show_outcomeBtn = document.getElementById("Outcome_input");
    let show_bothBtn = document.getElementById("both_input");
    let date_filterBtn = document.getElementById("date_filter");
    let amount_filterBtn = document.getElementById("amount_filter");
    let popup_settings = document.getElementById("popup_settings");
    let clearValues_settingsBtn = document.getElementById("clearValues_settings");
    let closePopup_settingsBtn = document.getElementById("closePopupBtn_settings");
    let addSettingsBtn = document.getElementById("Settings");


    // Event listeners
    if (addSettingsBtn) addSettingsBtn.addEventListener("click", Add_setting);
    if (closePopup_settingsBtn) closePopup_settingsBtn.addEventListener("click", closePopup_settings);
    if (clearValues_settingsBtn) clearValues_settingsBtn.addEventListener("click", clearValues_settings);
    if (show_inputBtn) show_inputBtn.addEventListener("click", showing_income);
    if (show_outcomeBtn) show_outcomeBtn.addEventListener("click", showing_outcome);
    if (show_bothBtn) show_bothBtn.addEventListener("click", showing_both);
    if (date_filterBtn) date_filterBtn.addEventListener("click", date_filter);
    if (amount_filterBtn) amount_filterBtn.addEventListener("click", amount_filter);
    if (closePopup_incomeBtn) closePopup_incomeBtn.addEventListener("click", closePopup_income);
    if (closePopup_outcomeBtn) closePopup_outcomeBtn.addEventListener("click", closePopup_outcome);
    if (loginBtn) loginBtn.addEventListener("click", login);
    if (singinBtn) singinBtn.addEventListener("click", sign_in);
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
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ id: id })
        }).then((_res) => {
          window.location.href = "/user_data?income=true&outcome=false&filterBy=date";
        }).catch((error) => {
          console.error("Error deleting income:", error);
        });
    }
    
    function deleteOutcome(id) {
        fetch("/delete-outcome", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ id: id })
        }).then((_res) => {
            window.location.href = "/user_data?income=false&outcome=true&filterBy=date";
        }).catch((error) => {
          console.error("Error deleting outcome:", error);
        });
    }
    
    document.querySelectorAll(".deleteIncome").forEach((button) => {
        button.addEventListener("click", () => {
          const id = button.getAttribute("data-id");
          deleteIncome(id);
        });
    });
    
    document.querySelectorAll(".deleteOutcome").forEach((button) => {
        button.addEventListener("click", () => {
          const id = button.getAttribute("data-id");
          deleteOutcome(id);
        });
    });
    


    function showing_income() {
        window.location.href = `/user_data?income=${encodeURIComponent(true)}&outcome=${encodeURIComponent(false)}&filterBy=date`;
      
    }
    
    function showing_outcome() {   
        window.location.href = `/user_data?income=${encodeURIComponent(false)}&outcome=${encodeURIComponent(true)}&filterBy=date`;
    }
    function showing_both() {   
        window.location.href = `/user_data?income=${encodeURIComponent(true)}&outcome=${encodeURIComponent(true)}&filterBy=date`;
    }
    function date_filter() {   
        window.location.href = `/user_data?income=${encodeURIComponent(true)}&outcome=${encodeURIComponent(true)}&filterBy=date`;
    }
    function amount_filter() {   
        window.location.href = `/user_data?income=${encodeURIComponent(true)}&outcome=${encodeURIComponent(true)}&filterBy=amount`;
    }
 




// פלאגין להוספת רקע מותאם לכל גרף
const customBackgroundPlugin = {
    id: 'customBackground',
    beforeDraw: (chart) => {
        const ctx = chart.ctx; // הקשר הציור של הגרף
        const { top, left, width, height } = chart.chartArea; // אזור הגרף
        ctx.save(); // שמירת מצב הקשר
        ctx.fillStyle = 'rgba(216, 214, 210, 0.92)'; // צבע הרקע
        ctx.fillRect(left, top, width, height); // ציור מלבן הרקע
        ctx.restore(); // שיחזור מצב הקשר
    }
};

// הגרף הראשון (bar chart)
const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['2020', '2021', '2022', '2023', '2024','2025'],
        datasets: [{
            label: 'Income per Year',
            data: income_of_year,
            backgroundColor: [
                'rgba(35, 2, 249, 0.94)',
                'rgba(247, 0, 0, 0.92)',
                'rgba(12, 235, 38, 0.92)',
                'rgba(17, 240, 240, 0.89)',
                'rgba(223, 11, 234, 0.94)',
                'rgba(245, 255, 64, 0.92)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: false
    },
    plugins: [customBackgroundPlugin]
});


// הגרף השני (line chart)
const ctx2 = document.getElementById('myChart2').getContext('2d');
const myChart2 = new Chart(ctx2, {
    type: 'line',
    data: {
        labels: ['2020', '2021', '2022', '2023', '2024','2025'],
        datasets: [{
            label: 'balance',
            data: sum_of_year,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 2,
            fill: true
        }]
    },
    options: {
        responsive: false
    },
    plugins: [customBackgroundPlugin]
});

// הגרף השלישי (pie chart)
const ctx3 = document.getElementById('myChart3').getContext('2d');
const myChart3 = new Chart(ctx3, {
    type: 'pie',
    data: {
        labels: ['Food', 'Rent'],
        datasets: [{
            data: outcome_by_category,
            backgroundColor: [
                'rgba(255, 99, 132, 0.8)',
                'rgba(54, 162, 235, 0.8)',
                // 'rgba(255, 206, 86, 0.8)',
                // 'rgba(75, 192, 192, 0.8)',
                // 'rgba(153, 102, 255, 0.8)',
                // 'rgba(255, 159, 64, 0.8)'
            ]
        }]
    },
    options: {
        responsive: false
    },
    plugins: [customBackgroundPlugin]
});

// הגרף הרביעי (doughnut chart)
const ctx4 = document.getElementById('myChart4').getContext('2d');
const myChart4 = new Chart(ctx4, {
    type: 'doughnut',
    data: {
        labels: ['Salary', 'Investments', 'Business'],
        datasets: [{
            data: income_by_category,
            backgroundColor: [
                // 'rgba(255, 99, 132, 0.8)',
                // 'rgba(54, 162, 235, 0.8)',
                'rgba(255, 206, 86, 0.8)',
                // 'rgba(75, 192, 192, 0.8)',
                'rgba(153, 102, 255, 0.8)',
                'rgba(255, 159, 64, 0.8)'
            ]
        }]
    },
    options: {
        responsive: false
    },
    plugins: [customBackgroundPlugin]
});


const ctx5 = document.getElementById('myChart5').getContext('2d');
const myChart5 = new Chart(ctx5, {
    type: 'bar',
    data: {
        labels: ['2020', '2021', '2022', '2023', '2024','2025'],
        datasets: [{
            label: 'Outcome per Year',
            data: outcome_of_year,
            backgroundColor: [
                'rgba(35, 2, 249, 0.94)',
                'rgba(247, 0, 0, 0.92)',
                'rgba(12, 235, 38, 0.92)',
                'rgba(17, 240, 240, 0.89)',
                'rgba(223, 11, 234, 0.94)',
                'rgba(245, 255, 64, 0.92)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: false
    },
    plugins: [customBackgroundPlugin]
});



});
