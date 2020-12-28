function [] = myplot(Filename,leg,save) 

%Parameters to the function:
%myplot(Filename,leg,save)
%The Filename variable requires a character array, which is the name of the file at which the figure is to be saved.
%Use leg=1 if legend is required, else leg=0
%Use save=1 if you would like to save the file, else save=0
%Below is an example script using this function at the last line of the script:
%addpath('D:\Dropbox\Dropbox\MMMRN 15 BATCH FGM\Codes_Used');
%x=[0:0.1:2];
%y{1}=x.^2;
%y{2}=x.^3;
%y{3}=x.^4;
%color='rgbymk';
%legends={'y=x^2' 'y=1+x^2' 'y=2+x^2'};
%figure();
%for i=1:3
%    plot(x,y{i},color(i),'linewidth',4,'displayname',legends{i});
%    hold on;
%end
%xlabel('X');
%ylabel('Y');
%legend('location','northwest');
%myplot('random.png',1,0);


legend('show');
DIMX = 6; DIMY =6;
set(gca,'Units', 'inches');
set(0, 'Units', 'inch');
BoxPos = [1, 1, DIMX, DIMY];
set(gca, 'Position', BoxPos);
monitorPos = get(0,'MonitorPositions');
% put the figure at the middle of the monitor
pos = [monitorPos(1, 3)/2-DIMX/2, monitorPos(1, 4)/2-DIMY/2];
outerpos = get(gca, 'OuterPosition');
if ~isempty(outerpos)
set(gca, 'OuterPosition',[0, 0, outerpos(3), outerpos(4)]);
set(gcf, 'Position', [100, 100, 700, 650]);
end
box on;
set(gca, 'FontName', 'Times New Roman','FontSize',20);
set(gca,'LineWidth',1.5);
set(gca,'XMinorTick','on','YMinorTick','on');
set(gca,'TickLength',[.02 .02]);
legend boxoff;
if leg == 0
    legend 'off'
end
if save == 1
    print(gcf, '-dpng', '-opengl', sprintf('-r%d', 600), Filename);
end
end