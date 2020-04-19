/*
* Initialize all Materialize elements
*/
function materializeInit() {
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.tooltipped').tooltip();
    $('.carousel').carousel();
    setInterval(function() {
        $('.carousel').carousel('next');
    }, 3000);
}
materializeInit();

/*
* Flash Messages
* Display for 3 seconds
*/
function flashMessage() {
    $("#flash_message").addClass("show");
    setTimeout(function () {
        $("#flash_message").removeClass("show");
    }, 3000);
}
flashMessage();