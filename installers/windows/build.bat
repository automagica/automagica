rem Copyright Oakwood Technologies BVBA 2020
call rmdir /S /Q build
call rmdir /S /Q wheels
call mkdir wheels
call cd ..
call cd ..
call pip wheel pip -w installers/windows/wheels
call pip wheel . -w installers/windows/wheels
call cd installers/windows
call pip install -r requirements.txt
call pynsist setup.cfg