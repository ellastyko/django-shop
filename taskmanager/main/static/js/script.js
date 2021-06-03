
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$('#lang').click((e) => {
    if ($('html').attr("lang") == 'en') {
        $('html').attr("lang", 'ru');
        $('#lang').val('RU')
    }      
    else if ($('html').attr("lang") == 'ru') {
        $('html').attr("lang", 'en');
        $('#lang').val('EN')
    }      
})