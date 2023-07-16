// Check if the current device is a mobile device
function isMobileDevice() {
    return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
}

// Redirect to the mobile version of the website if it's a mobile device and not already on the mobile version
if (isMobileDevice() && !window.location.href.includes("/mobile")) {
    var mobileUrl = "/mobile"; // Replace with the URL of your mobile website
    window.location.href = mobileUrl;
}
