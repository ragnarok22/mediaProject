$(document).ready(function () {
    pass = $("#password");
    pass_check = $("#password-check");
    sex = $("#sex");
    date = $("#date");

    $("#create").click(function (event) {
        //date.val() -----> year-moth-day
        if(pass.val() != pass_check.val()){
            error_message("Las contraseñas no coinciden");
        }
        if(sex.val() == "undefined"){
            error_message("Debe de seleccionar su sexo");
        }
    });

    function error_message(message){
        toastr.options.closeButton = true;
        toastr.options.positionClass = 'toast-top-right';
        toastr.error(message);
        event.preventDefault();
    }
});