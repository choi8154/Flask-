document.getElementById("signupForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = {
        login_id: document.getElementById("login_id").value,
        password: document.getElementById("password").value,
        email: document.getElementById("email").value,
        name: document.getElementById("name").value,
        phone: document.getElementById("phone").value
    };

    const response = await fetch("/signup/", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    if (response.ok) {
        document.getElementById("result").innerText = "회원가입 성공!";
        setTimeout(() => { window.location.href = "/signin"; }, 1000); 
    } else {
        const result = await response.json();
        document.getElementById("result").innerText = result.error;
    }
});