import answerStyles from  '../styles/answerSection.module.css';
import { useSelector } from 'react-redux';
import type { RootState } from '../app/store';
import styles from '../styles/answerSection.module.css';

export function AnswerSection() {

  const summaries = useSelector((state: RootState) => state.chat.summaries);
  const inputTexts = useSelector((state: RootState) => state.chat.inputTexts);

  return (
    <div className={answerStyles.answerSection}>
      {inputTexts.map((text, index) => (
      <div className={styles.chatItem} key={index}>
        <p className={styles.userInput}>{text}</p>
        <p className={styles.summary}>{summaries[index]}</p>
      </div>
      ))}
    </div>
  )
}