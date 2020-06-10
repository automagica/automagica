rem Copyright Oakwood Technologies BVBA 2020
call rmdir /S /Q build
call rmdir /S /Q wheels
call mkdir wheels
call cd wheels
call pip wheel pip
call pip wheel pywin32
call pip wheel git+https://github.com/automagica/automagica@v3.0
call cd ..
call pip install pynsist==2.4
call pynsist setup.cfg