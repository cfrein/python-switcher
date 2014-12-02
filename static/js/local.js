/*global $SCRIPT_ROOT, $ */

$(
    // When the LED button is pressed (change)
    // do an ajax request to server to change LED state
    function () {
        "use strict";
        $('#flip-1').change(function () {
            $.getJSON($SCRIPT_ROOT + '/_led', {
                state: $('#flip-1').val()
            });
        });
    }
);

// Send value if selector is tapped
$(
    function () {
        "use strict";
        $('#selector1').change(function () {
            $.getJSON($SCRIPT_ROOT + '/_led', {
                state: $('#selector1').val()
            });
        });
    }
);

$(
    // Button has been clicked
    function clickedOp() {
        "use strict";
        $.ajax({
            url: $SCRIPT_ROOT + '/_button'
        });
    }
);