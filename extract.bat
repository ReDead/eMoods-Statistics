@echo off

for /r %%F in (*.emoods) do (
    tar -xf "%%F" -C eMoods-data
)

del *.emoods

echo Unzipping .emoods files completed.