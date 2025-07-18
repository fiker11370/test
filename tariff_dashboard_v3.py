




# Time series plot of dollar impact
impact_over_time = filtered_df.groupby("Date")["Dollar Impact"].sum().reset_index()
impact_fig = px.line(
    impact_over_time,
    x="Date",
    y="Dollar Impact",
    title="Estimated Dollar Impact to Industrials Over Time"
)
st.plotly_chart(impact_fig)
