$(document).ready(function () {
    join_click_by_ajax("#terms", "#terms-content", "/terms");
    join_click_by_ajax("#privacy", "#privacy-content", "/privacy");
    join_click_by_ajax("#about", "#about-content", "/about");
    join_click_by_ajax("#contact", "#contact-content", "/contact/us");

    loader = $('#spinner-users-in');
    loader.css('display', 'inline');
    $('#users-in').load('/users/in', function () {
        loader.css('display', 'none');
    });

    loaderStaff = $('#spinner-users-staff-in');
    loaderStaff.css('display', 'inline');
    $('#users-staff-in').load('/users/staff/in', function () {
        loaderStaff.css('display', 'none');
    });
});

function print(sms){
    console.log(sms);
}

function join_click_by_ajax(to, from, context){
    $(to).click(function (event) {
        event.preventDefault();
        loader = $('#spinner-' + to.substr(1));
        loader.css('display', 'inline');
        $(from).load(context, function () {
            loader.css('display', 'none');
        });
    });
}
