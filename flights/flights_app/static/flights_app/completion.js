"use strict";

$('html').on('click', function(event) {
    if (event.type !== 'focus')
        $('.completion_tooltip').remove();
});

var make_completion = function(params) {
    var fields_vals = $(params.fields_selector)
            .on('input focus', function() {
                var target = this;
                process_variants(
                        function(data) {
                            if (data.length === 1)
                                params.on_completion(data);
                            else
                                build_tooltip(data, target);
                        }
                );
            })
            .get();
    var keys = $.map(fields_vals, function(field) {
        return field.name;
    });
    var fields = {};
    for (var i in keys) {
        fields[keys[i]] = fields_vals[i];
    }
    function build_tooltip(variants, target) {
        $('.completion_tooltip').remove();
        var html = '<div class="completion_tooltip">';
        html += '<ul>';
        for (var i in variants) {
            html += '<li>' + variants[i][target.name] + '</li>';
        }
        html += '</ul>';
        html += '</div>';
        console.log(html);
        $(html).appendTo($(target).parent()).find('li')
                .click(function() {
                    $(target).val($(this).html()).trigger('input');
                });

    }
    function process_variants(next_action) {
        var data = {};
        for (var i in keys) {
            data[keys[i]] = fields[keys[i]].value;
        }
        $.getJSON(params.completion_url, data, function(variants, sts) {
            next_action(variants); // TODO: check if request succeded
        });
    }
};

var params = {
    completion_url: 'autocomplete',
    fields_selector: '#completion_fields input[type=text]',
    on_completion: function(completions) {
        if (completions.length === 1) {
            var air = completions[0];
            map.setCenter(new google.maps.LatLng(air.lat, air.lon));
        }
    }
};

$(document).ready(function() {
    make_completion(params);
});
