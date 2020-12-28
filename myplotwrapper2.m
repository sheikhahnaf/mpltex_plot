addpath("/home/alvi/utils/project/csnw/output/tensiontest/graph")
data2 = load('gold600.txt')
data3 = load('silver600.txt')
data4 = load('auag600.txt')
data5 = load('agau600.txt')
color='rgbmyk'
#legends={'300k','500k','600k','700k'}
legends={'Gold','Silver','Gold-Silver','Silver-Gold'}
figure()
y{1}= data2(:,4)*200*200/(3.1416*55*55)
y{2}= data3(:,4)*200*200/(3.1416*55*55)
y{3}= data4(:,4)*200*200/(3.1416*55*55)
y{4}= data5(:,4)*200*200/(3.1416*55*55)
for i=1:4
    plot(data2(:,1),y{i},color(i),'linewidth',4,'displayname',legends{i})
    hold on
end    
box on
xlabel('strain')
ylabel('stress(GPa)')
legend('location','northwest')
axis ([0 0.2 0 5])
myplot('T600.png',1,1)