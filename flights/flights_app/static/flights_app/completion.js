"use strict";

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
                    .on('blur', function(){
                $('.completion_tooltip').slideUp('slow', function(){$(this).remove();});
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
//        $('.completion_tooltip').remove();
        var html = '<div class="completion_tooltip">';
        html += '<ul>';
        for (var i in variants) {
            html += '<li>' + variants[i][target.name] + '</li>';
        }
        html += '</ul>';
        html += '</div>';
//        console.log(html);
        $(html).appendTo($(target).parent()).hide(0, function(){$(this).slideDown('slow');}).find('li')
                .mousedown(function() {
                    $(target).val($(this).html());
                    process_variants(
                            function(data) {
                                if (data.length === 1)
                                    params.on_completion(data);

                            }
                    );
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
    on_completion: (function() {
        var marker;
        return function(completions) {
            if (completions.length === 1) {
                if (marker)
                    marker.setMap(null);
                var air = completions[0];
                var pos = new google.maps.LatLng(air.lat, air.lon);
                marker = new google.maps.Marker({
                    position: pos,
                    title: air.name,
                    map: map
                });
                map.setCenter(pos);
            }
        };
    })()
};

$(document).ready(function() {
    make_completion(params);
});
