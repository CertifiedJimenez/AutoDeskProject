$(document).ready(function() {
    //Built in search function
    $( "#search-btn" ).click(function() {					
        Job = $('#intro-keywords').val()
        Location = $('#autocomplete-input').val()
        search_url = '/search/'+Job+'/'+Location+'/1'
        window.open(search_url,"_self")
    });
});