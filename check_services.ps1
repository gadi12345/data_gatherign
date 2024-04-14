$serviceName = "Windows Update"
$serviceStatus = Get-Service -Name $serviceName


if($serviceStatus){
    $status = $serviceStatus.Status

    if($serviceName-eq "DHCP Client"){
        if ($status-eq"Stopped") {
          Write-Host "service '$serviceName' stopped."
     }
    }
    Write-Host "service '$serviceName' has status '$status'"
}