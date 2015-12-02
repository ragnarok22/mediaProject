$(document).ready(function () {
    pass = $("#password");
    pass_check = $("#password-check");
    sex = $("#sex");
    date = $("#date");
    var systemdate = new Date();
    year = systemdate.getFullYear();

    $("#create").click(function (event) {
        //date.val() -----> year-moth-day
        if(pass.val() != pass_check.val()){
            error_message("Las contraseñas no coinciden");
        }
        if(sex.val() == "U"){
            error_message("Debe de seleccionar su sexo");
        }
        if(parseInt(date.val().substr(0, 4)) >= year){
            error_message("El año debe ser menor que la fecha actual");
        }
    });

    function error_message(message){
        toastr.options.closeButton = true;
        toastr.options.positionClass = 'toast-top-right';
        toastr.error(message);
        event.preventDefault();
    }
});