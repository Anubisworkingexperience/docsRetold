import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";

interface ChatState {
  inputTexts: string[];
  summaries: string[];
}

const initialState : ChatState = {
  inputTexts: [],
  summaries: [],
}

const chatSlice = createSlice({
  name: 'chat',
  initialState,
  reducers: {
    addInputText(state, action: PayloadAction<string>) {
      state.inputTexts.push(action.payload);
    },
    addSummary(state, action: PayloadAction<string>) {
      state.summaries.push(action.payload);
    },
    clearChat(state) {
      state.inputTexts = [];
      state.summaries = [];
    }
  },
});

export const { addInputText, addSummary, clearChat } = chatSlice.actions;

export default chatSlice.reducer;