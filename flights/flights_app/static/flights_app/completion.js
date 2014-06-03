Completer = function(){
    this.selected = false;
    this.lookup_url = 'autocomplete';
    this.fields = $('#completion_fields input[type=text]').get();
    this.keys = $.map(this.fields, function(field){ return field.name });
    this.make_tooltip(candidates){
        html = '<div class="completion_tooltip">'
        html += '<ul>'
        for(c in candidates){
            html += '<li>' + c + '</li>';
        }
        html += '</ul>'
        html += '</div>'
        return html;
    }


}

var cmplt;

$('document').ready(function(){
    cmplt = new Completer;
});
