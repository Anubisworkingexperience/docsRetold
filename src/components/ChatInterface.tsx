import '../styles/chatInterface.module.css'
import styles from '../styles/chatInterface.module.css';

export function ChatInterface() {
  return (
    <div className={styles.chatInterface}>
      <textarea name="chat" id="chat" className={styles.userInput}></textarea>
    </div>
  )
}