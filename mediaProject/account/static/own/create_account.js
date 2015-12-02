$(document).ready(function () {
    pass = $("#password");
    pass_check = $("#password-check");
    sex = $("#sex");
    console.log(sex.val());

    $("#create").click(function (event) {
        if(pass.val() != pass_check.val()){
            alert("las contrasenas no coinciden");
            event.preventDefault();
        }
    });
});