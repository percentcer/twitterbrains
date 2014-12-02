$(document).ready( function() {
    $('#cli').on('submit', function(e){
        e.preventDefault();
        $.ajax({
            type: "POST",
            cache: false,
            url: $(this).attr('action'),
            data: $(this).serialize(),
            success: function(data){
                $("#responses").append("<p class='stimulus'>" + $("#input").val() + "</p>");
                $("#responses").append("<p class='response'>" + data + "</p>");
                $("#input").val("");
            }
        });
    });
});