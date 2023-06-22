function createEmail(email, password, quota, domain) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/cpsess7102702315/execute/Email/add_pop");
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    var emailData = "email=" + encodeURIComponent(email) +
                    "&password=" + encodeURIComponent(password) +
                    "&quota=" + encodeURIComponent(quota) +
                    "&domain=" + encodeURIComponent(domain) +
                    "&send_welcome_email=1";
  
    xhr.send(emailData);
}

createEmail("cobain", "1234556", "250", "lasernailtherapy.com");
