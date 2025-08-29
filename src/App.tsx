import { ChatInterface } from "./components/ChatInterface"
import { AnswerSection } from "./components/AnswerSection";
import './styles/app.module.css'
import styles from './styles/app.module.css';

function App() {

  return (
    <>
      <div className={styles.app}>
        <h1>DocsRetold</h1>
        <p className={styles.greeting}>Hello! I can help you summarize your text!</p>
        <AnswerSection />
        <ChatInterface />
      </div>
    </>
  )
}

export default App
