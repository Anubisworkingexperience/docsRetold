import '../styles/chatInterface.module.css';
import styles from '../styles/chatInterface.module.css';
import arrowUp from '../assets/arrow-up.svg'
import { useState } from 'react';

export function ChatInterface() {

  const [messageSent, setMessageSent] = useState<boolean>(false);
  const [inputText, setInputText] = useState<string>('');
  const [summary, setSummary] = useState<string | null>(null);

  const sendSummarizeRequest = async function() {
    if (!inputText.trim()) return;

    try {
      const response = await fetch('http://localhost:8000/summarize', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          article: inputText,
          max_length: inputText.length / 2,
          min_length: 30,
          do_sample: false,
        }),
      });

      const data = await response.json();
      setSummary(data.summary);
      setMessageSent(true);
    } 
    catch(err) {
      console.error('Error sending a request to model', err);
    }
  }

  return (
    <div className={styles.chatInterface}>
      <div className={styles.inputWrapper}>
        <textarea name="chat" id="chat" className={styles.userInput}
         onChange={(e) => setInputText(e.target.value)}></textarea>
        <img src={arrowUp} alt="send button" className={styles.sendButton}
         onClick={sendSummarizeRequest}/>
      </div>
    </div>
  )
}