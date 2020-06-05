rem Copyright Oakwood Technologies BVBA 2020
call conda env remove -n automagica
call conda create -n automagica python=3.7.5 --yes
call conda activate automagica
call pip install automagica
call rmdir /S /Q build
call rmdir /S /Q wheels
call mkdir wheels
call cd wheels
call pip freeze > requirements.txt
call pip wheel pip
call pip wheel -r requirements.txt --no-binary automagica
call cd ..
call pip install pynsist==2.4
call pynsist setup.cfg
call conda deactivate