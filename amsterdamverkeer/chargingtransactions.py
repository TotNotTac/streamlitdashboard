
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from loaddata import *


def chargingtransactionsplot():
    transacties = load_transactions()

    chargeTab, connectedTimeTab = st.tabs(
        ["Total charging points", "Connected time and charge time distributions"])

    with connectedTimeTab:
        col1, col2 = st.columns([3, 4])

        with col1:
            st.markdown("""
            ### Distribution of charging- & connnected times
            The following plot shows two different distributions; the distribution of the time 
                        charged and the distribution of the time that a charger was connected to a chargepoint.
            """)

        with col2:
            logCol, overlayCol = st.columns(2)
            with logCol:
                logscale = st.checkbox("Logarithmic scale", value=True)
            with overlayCol:
                overlay = st.checkbox("Overlay plots", value=False)

            if overlay:
                plt.hist(transacties['ConnectedTime'],
                         label="Connected time", color="orange")
                plt.hist(transacties['ChargeTime'],
                         label="Charge time", color="blue")
                plt.legend()
            else:
                fig, axs = plt.subplots(1, 2, sharey=True, sharex=True)

                axs[0].hist(transacties['ChargeTime'],
                            label="Charge time", color="blue")
                axs[1].hist(transacties['ConnectedTime'],
                            label="Connected time", color="orange")
                fig.legend()
            if logscale:
                plt.yscale('log')
            st.pyplot()

    with chargeTab:
        col1, col2 = st.columns([3, 4])

        with col1:
            st.markdown("""
            ### Distribution of charging- & connnected times
            
            The following chart demonstrates the correlation between the total amount of charging transactions and the total energy charged.
            Surprisingly neither the amount of transactions nor the amount of energy charged increases exponantially, rather it increases
            linearly every year with roughly the same amount.
            """)

        with col2:
            transacties = transacties.sort_values('Ended')
            transacties['count'] = 1
            transacties['count'] = transacties['count'].cumsum()

            transacties['TotalEnergy_cumm'] = transacties['TotalEnergy'].cumsum()

            # sns.lineplot(transacties, x='Ended', y='TotalEnergy_cumm')
            # sns.lineplot(transacties, x='Ended', y='count')

            fig = plt.figure()
            ax1 = fig.add_subplot(111)
            ax1.plot(transacties['Ended'], transacties['TotalEnergy_cumm'])
            ax1.set_ylabel('Total energy charged')

            ax2 = ax1.twinx()
            ax2.plot(transacties['Ended'], transacties['count'], 'r-')
            ax2.set_ylabel('Charge transaction count')
            for tl in ax2.get_yticklabels():
                tl.set_color('r')
            fig.legend(["Total energy charged", "Charge transaction count"])

            st.pyplot()
