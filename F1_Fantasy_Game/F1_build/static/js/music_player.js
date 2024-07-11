const audio = document.getElementById('myAudio');

        function toggleAudio() {
            if (audio.paused) {
                audio.play();
            } else {
                audio.pause();
            }
        }
        
// const audio = document.getElementById('myAudio');
        // function playAudio() {
        //     audio.play();
        // }

        // function pauseAudio() {
        //     audio.pause();
        // }

        // function stopAudio() {
        //     audio.pause();
        //     audio.currentTime = 0;
        // }