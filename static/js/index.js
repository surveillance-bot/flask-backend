console.log("hsdpla[psd")

$(document).on("change", ".file_multi_video", function (evt) {
    var $pre = $('#video_here');
    $pre[0].src = URL.createObjectURL(this.files[0]);
    $pre.parent()[0].load();
});

document.getElementById('submit').addEventListener('click', function () {
    console.log("dkasnjdhasjd")
    var files = document.getElementById('input').files;
    if (files.length > 0) {
        var reader = new FileReader();
        reader.readAsDataURL(files[0]);
        var text;
        reader.onload = function () {
            text = reader.result;
            document.getElementById("video").value = text
        };
        
        reader.onerror = function (error) {
            console.log('Error: ', error);
        };
    }
});

