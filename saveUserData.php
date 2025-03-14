<?php
if (isset($_POST['name']) && isset($_POST['dob'])) {
    // Retrieve and sanitize input (add more sanitization as needed)
    $name = strip_tags(trim($_POST['name']));
    $dob = strip_tags(trim($_POST['dob']));
    
    // Prepare data to be saved
    $data = "Name: " . $name . "\nBirthday: " . $dob;
    
    // Create a filename using the name, replacing spaces with underscores
    $filename = preg_replace('/\s+/', '_', $name) . "_bday.txt";
    
    // Define the directory where you want to save the file
    // Make sure the server has write permissions to this directory
    $directory = "user_data/";
    
    // Create directory if it doesn't exist
    if (!is_dir($directory)) {
        mkdir($directory, 0755, true);
    }
    
    // Write the file to the server
    $filepath = $directory . $filename;
    if (file_put_contents($filepath, $data)) {
        echo "Data saved successfully.";
    } else {
        echo "Error saving data.";
    }
} else {
    echo "Error: Missing name or dob.";
}
?>
