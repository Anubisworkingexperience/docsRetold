import '../styles/chatInterface.module.css';
import styles from '../styles/chatInterface.module.css';
import arrowUp from '../assets/arrow-up.svg';
import { useDispatch } from 'react-redux';
import { addInputText, addSummary } from '../features/chat/chatSlice';
// import type { RootState } from '../app/store';
import { useState } from 'react';

export function ChatInterface() {

  const dispatch = useDispatch();
  // const inputText = useSelector((state: RootState) => state.chat.inputText);
  const [currentInput, setCurrentInput] = useState<string>('');

  const sendSummarizeRequest = async function() {
    if (currentInput.length <= 0) return;

    dispatch(addInputText(currentInput));

    try {
      const response = await fetch('http://localhost:8000/summarize', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          article: currentInput,
          max_length: Math.floor(currentInput.length / 2),
          min_length: 30,
          do_sample: false,
        }),
      });

      const data = await response.json();
      dispatch(addSummary(data.summary));
      // setMessageSent(true);
    } 
    catch(err) {
      console.error('Error sending a request to model', err);
    }

    setCurrentInput('');
  }

  return (
    <div className={styles.chatInterface}>
      <div className={styles.inputWrapper}>
        <textarea name="chat" id="chat" className={styles.userInput}
         onChange={(e) => setCurrentInput(e.target.value)} onKeyDown={(e) => {
          if (e.key == 'Enter' && !e.repeat && !e.shiftKey) {
            e.preventDefault();
            sendSummarizeRequest();
          }
         }}></textarea>
        <img src={arrowUp} alt="send button" className={styles.sendButton}
         onClick={sendSummarizeRequest}/>
      </div>
    </div>
  )
}