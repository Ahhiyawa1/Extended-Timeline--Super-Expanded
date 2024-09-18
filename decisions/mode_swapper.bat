@echo off
echo This script will change the mode at which No Governing Capacity [Classic] operates.
echo DEFAULT: AI cannot increase its Governing Capacity.
echo 1: AI cannot increase its Governing Capacity.
echo 2: AI can increase its Governing Capacity.
echo 3: Reset the decisions files (will revert back to mode 1 and restore broken files if corrupted or missing)
echo.
goto await
:await
set /p choice=PRESS 1 OR 2 AND CONFIRM USING ENTER: 
if %choice%==1 (
    if exist ngcl_decisions.txt (
        echo The mode you've selected is already picked, exit the script or try again.
        goto await
    ) else (
        if exist ngcl_decisions.txt.bak (
            if exist ngclai_decisions.txt (
                cls
                ren ngcl_decisions.txt.bak ngcl_decisions.txt
                ren ngclai_decisions.txt ngclai_decisions.txt.bak
                ping -n 2 127.0.0.1 > nul
                echo No Governing Capacity [Classic] now runs at mode 1: AI cannot increase its Governing Capacity.
                echo.
                pause
            ) else (
                cls
                echo ERROR! File named ngclai_decisions.txt was not found.
                echo Either rename the files back manually or use mode 3 to restore the files.
                echo.
                pause
            )
        ) else (
            cls
            echo ERROR! File named ngcl_decisions.txt.bak was not found.
            echo Either rename the files back manually or use mode 3 to restore the files.
            echo.
            pause
        )
    )
) else (
    if %choice%==2 (
        if exist ngclai_decisions.txt (
            echo The mode you've selected is already picked, exit the script or try again.
            goto await
        ) else (
            if exist ngclai_decisions.txt.bak (
                if exist ngcl_decisions.txt (
                    cls
                    ren ngcl_decisions.txt ngcl_decisions.txt.bak
                    ren ngclai_decisions.txt.bak ngclai_decisions.txt
                    ping -n 2 127.0.0.1 > nul
                    echo No Governing Capacity [Classic] now runs at mode 2: AI can increase its Governing Capacity.
                    echo.
                    pause
                ) else (
                    cls
                    echo ERROR! File named ngcl_decisions.txt was not found.
                    echo Either rename the files back manually or use mode 3 to restore the files.
                    echo.
                    pause
                )
            ) else (
                cls
                echo ERROR! File named ngclai_decisions.txt.bak was not found.
                echo Either rename the files back manually or use mode 3 to restore the files.
                echo.
                pause
            )
        )
    ) else (
        if %choice%==3 (
            cls
            echo Removing old files...
            ping -n 2 127.0.0.1 > nul
            del /F /Q ngclai_decisions.txt > nul 2> nul
            del /F /Q ngclai_decisions.txt.bak > nul 2> nul
            del /F /Q ngcl_decisions.txt > nul 2> nul
            del /F /Q ngcl_decisions.txt.bak > nul 2> nul
            echo Removed old files.
            echo Copying from backup...
            ping -n 2 127.0.0.1 > nul
            attrib -h ngcl.bak
            attrib -h ngclai.bak
            copy ngcl.bak ngcl_decisions.txt > nul 2> nul
            copy ngclai.bak ngclai_decisions.txt.bak > nul 2> nul
            attrib +h ngcl.bak
            attrib +h ngclai.bak
            echo Copied from backup.
            echo. 
            echo Files have been restored! Mode 1 selected by default.
            pause
        ) else (
            echo Wrong number specified, pick either 1 or 2 or 3.
            goto await
        )
    )
)