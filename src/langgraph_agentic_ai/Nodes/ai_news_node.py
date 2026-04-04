from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate
import os
from src.langgraph_agentic_ai.State.AINewsState import AINewsState


class AINewsNode:

    def __init__(self, llm):
        self.llm = llm
        self.tavily_client = TavilyClient()
        ### this is used to capture various steps in this file so that later can be use for steps shwon

    def fetch_news(self, state: AINewsState) -> dict:
        """
        Fetch AI news basedon the specified frequency.
        Args:
            state (dict): the state dictionary containly 'frequency'
        Returns:
            dict: updated state with 'news'_data key containing fetched news data.
        """
        frequency = state["frequency"].lower()
        time_range_map = {"daily": "d", "weekly": "w", "monthly": "m", "yearly": "y"}
        days_map = {"daily": 1, "weekly": 7, "monthly": 30, "yearly": 365}
        response = self.tavily_client.search(
            query="Top Artificial Intelligence(AI) news India and globally",
            topic="news",
            time_range=time_range_map[frequency],
            include_answer="advanced",
            max_results=15,
            days=days_map[frequency],
        )
        return {"news_data": response.get("results", [])}

    def summarize_news(self, state: AINewsState) -> dict:
        """
        Summarize the fetched news data using an LLM.
        Args:
            state (dict): the state dictionary containly 'news_data'
        Returns:
            dict: updated state with 'summary' key containing summarized news data.
        """
        news_data = state["news_data"]
        prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """ Summarize AI news articles into markdown format. for each item include:
            - Date in ** YYYY-MM-DD** formate in IST timezone.
            - Conside sentences summary from latest news articles
            - Sort news by data wise (latest first)
            - Source URL as a link
            
            Use Format:
            ### [Date]
            - Summary : [Summary]
            - URL : [url]""",
                ),
                ("user", "Here is the news data: {articles}"),
            ]
        )
        article_str = "\n\n".join(
            [
                f"Content: {item.get('content', '')} \n url : {item.get('url', '')} \n Date : {item.get('published_date', '')}"
                for item in news_data
            ]
        )
        chain = prompt_template | self.llm
        summary = chain.invoke({"articles": article_str})
        return {"summary": summary.content}

    def save_result(self, state: AINewsState) -> dict:
        """
        Save the summarized news data to a file.
        Args:
            state (dict): the state dictionary containly 'summary'
        Returns:
            dict: updated state with 'result' key containing summarized news data.
        """
        frequency = state["frequency"]
        summary = state["summary"]
        os.makedirs("./AI_NEWS_SUMMARY", exist_ok=True)
        with open(f"./AI_NEWS_SUMMARY/{frequency}_ai_news_summary.md", "w") as f:
            f.write(summary)
        return {"saved_file_name": f"./AI_NEWS_SUMMARY/{frequency}_ai_news_summary.md"}
