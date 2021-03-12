echo off
ZipCode=${1}
ZipCode1=${2}

sh /Applications/SoapUI-5.5.0.app/Contents/java/app/bin/testrunner.sh -sVerifyData -a -f/Users/joaocerqueira/Desktop/ResultsCli -GZipCode=${ZipCode} -GZipCode1=${ZipCode1}  /Users/joaocerqueira/Downloads/DesafioSoapUI-soapui-project.xml