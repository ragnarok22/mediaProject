$(document).ready(function () {
    pass = $("#password");
    pass_check = $("#password-check");
    sex = $("#sex");
    console.log(sex.val());

    $("#create").click(function (event) {
        if(pass.val() != pass_check.val()){
            toastr.options.closeButton = true;
            toastr.options.positionClass = 'toast-top-right';
            toastr.error("Las contraseñas no coinciden");
            event.preventDefault();
        }
        if(sex.val() == "undefined"){
            toastr.options.closeButton = true;
            toastr.options.positionClass = 'toast-top-right';
            toastr.error("Debe de seleccionar su sexo");
            event.preventDefault();
        }
    });
});