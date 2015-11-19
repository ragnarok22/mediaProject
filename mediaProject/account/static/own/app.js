$(document).ready(function () {
    join_click_by_ajax("#terms", "#terms-content", "/terms");
    join_click_by_ajax("#privacy", "#privacy-content", "/privacy");
    join_click_by_ajax("#about", "#about-content", "/about");
    join_click_by_ajax("#contact", "#contact-content", "/contact/us");

    join_click_by_ajax("#profile", "#information", "/profile/1", "#spinner-information");

    //mostrar los usuarios que se encuentran en linea
    loader = $('#spinner-users-in');
    loader.css('display', 'inline');
    $('#users-in').load('/users/in', function () {
        loader.css('display', 'none');
    });

    //mostrar los administradores que se encuentran en linea
    loaderStaff = $('#spinner-users-staff-in');
    loaderStaff.css('display', 'inline');
    $('#users-staff-in').load('/users/staff/in', function () {
        loaderStaff.css('display', 'none');
    });

    //mostrar la informacion reciente
    loaderInfo = $('#spinner-information');
    loaderInfo.css('display', 'inline');
    $('#information').load('/informations', function () {
        loaderInfo.css('display', 'none');
    });
});

function print(sms){
    console.log(sms);
}

function join_click_by_ajax(to, from, context, load){
    $(to).click(function (event) {
        event.preventDefault();
        if (load == null){
            loader = $('#spinner-' + to.substr(1));
        }else{
            loader = $(load);
        }
        loader.css('display', 'inline');
        $(from).load(context, function () {
            loader.css('display', 'none');
        });
    });
}
