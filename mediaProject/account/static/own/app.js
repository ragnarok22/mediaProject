$(document).ready(function () {
    join_by_ajax("#terms", "#terms-content", "/terms");
    join_by_ajax("#privacy", "#privacy-content", "/privacy");
    join_by_ajax("#about", "#about-content", "/about");
    join_by_ajax("#contact", "#contact-content", "/contact/us");
});

function print(sms){
    console.log(sms);
}

function join_by_ajax(to, from, context){
    $(to).click(function (event) {
        event.preventDefault();
        loader = $('#spinner-' + to.substr(1));
        loader.css('display', 'inline');
        $(from).load(context, function () {
            loader.css('display', 'none');
        });
    });
}