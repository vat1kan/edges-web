window.addEventListener('scroll', function() {
    var navbar = document.getElementById('navbar');
    if (window.scrollY > 50) { // Adjust the value as needed
      navbar.style.backgroundColor = 'rgba(0, 0, 0, 0.8)'; // Change to desired background color
    } else {
      navbar.style.backgroundColor = 'transparent';
    }
  });

function toggleNoiseFields() {
    var checkbox = document.getElementById("noise_check");
    var noiseFields = document.getElementById("noise_fields");
    var noiseType = document.getElementById("noise_type").value;
    var noiseParameterInput = document.getElementById("noise_parameter");

    if (checkbox.checked) {
        noiseFields.style.display = "block";
        if (noiseType === "gauss") {
            noiseParameterInput.setAttribute("min", "0");
            noiseParameterInput.setAttribute("max", "100");
            noiseParameterInput.setAttribute("step", "5");
        } else {
            noiseParameterInput.setAttribute("min", "0");
            noiseParameterInput.setAttribute("max", "1");
            noiseParameterInput.setAttribute("step", "0.05");
        }
    } else {
        noiseFields.style.display = "none";
    }
}

function toggleGroundTruthField() {
    var metricsCheck = document.getElementById("calculate_metrics");
    var metricsFields = document.getElementById('metrics_fields');
    var groundTruthInput = document.getElementsByName("ground_truth")[0];

    if (metricsCheck.checked) 
    {
        metricsFields.style.display = 'block';
        groundTruthInput.required = true
    } 
    else 
    {
        metricsFields.style.display = 'none';
        groundTruthInput.required = false;
    }
}

function validateForm() {
    var metricsCheck = document.getElementById("calculate_metrics");
    var mainFilesInput = document.getElementsByName("file")[0];
    var mainFiles = mainFilesInput.files;
    var gtFilesInput = document.getElementsByName("ground_truth")[0];
    var gtFiles = gtFilesInput.files;

    if (mainFiles.length === 0) {
        alert("Please upload at least one image.");
        return false;
    }

    if (mainFiles.length > 30) {
        alert("You can upload at most 30 images.");
        return false;
    }

    for (var i = 0; i < mainFiles.length; i++) 
    {
        if (mainFiles[i].size > 5 * 1024 * 1024 || gtFiles[i].size > 5 * 1024 * 1024) 
        {
            alert("Image size should be less than 5 MB.");
            return false;
        }
    }

    if (metricsCheck.checked) 
    {
        var groundTruthFiles = document.getElementsByName("ground_truth")[0].files;

        if (mainFiles.length !== groundTruthFiles.length) {
            alert("Number of original images must match number of ground truth images.");
            return false;
        }

        return true;
    }
}
